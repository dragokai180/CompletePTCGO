from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5c0c36a-8718-5e11-ab06-08c7c031e009',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name',
    display_name='Cacturne',
    searchable_by=['Cacturne', 'Stage 1', 'Cacturne'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name',
    family_id=331,
    abilities=[
        Ability(
            title='Poison Payback',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), the Attacking Pokémon is now Poisoned."),
        ),
        Attack(
            title='Feint Attack',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. This damage isn't affected by Weakness, Resistance, or any other effects on that Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
