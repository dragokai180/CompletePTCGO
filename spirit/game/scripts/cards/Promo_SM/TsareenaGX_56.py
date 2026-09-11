from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f2c11361-ca14-5028-b624-4d9259aa460a',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TsareenaGX.Name',
    display_name='Tsareena-GX',
    searchable_by=['Tsareena-GX', 'Stage 2', 'GX', 'TsareenaGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=56,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    family_id=763,
    abilities=[
        Attack(
            title='Side Eye',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. The new Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Jumping Side Kick',
            game_text="If your opponent's Active Pokémon is Confused, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title="Queen's Command-GX",
            game_text="Your opponent discards 4 cards from their hand. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
