from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a1cfff77-c983-535d-a7c0-adc034013271',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowakGX.Name',
    display_name='Alolan Marowak-GX',
    searchable_by=['Alolan Marowak-GX', 'Stage 1', 'GX', 'AlolanMarowakGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=187,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    family_id=105,
    abilities=[
        Ability(
            title='Cursed Body',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Confused.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Confused."),
        ),
        Attack(
            title='Fiery Bone',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
        Attack(
            title='Lost Boomerang-GX',
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. This damage isn't affected by Weakness or Resistance. If a Pokémon is Knocked Out by this damage, put that Pokémon and all cards attached to it in the Lost Zone instead of the discard pile. (You can't use more than 1 GX attack in a game.)",
            cost={},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
