from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c440d3e-54b2-5b0a-8ecd-64e848013588',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    display_name='Poliwag',
    searchable_by=['Poliwag', 'Basic', 'Poliwag'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=60,
    abilities=[
        Ability(
            title="Round ‘n' Round",
            game_text="You can use this Ability only if you go second. Once during your first turn (before your attack), you may leave your opponent's Active Pokémon Confused.",
            passive=standard_passive("You can use this Ability only if you go second. Once during your first turn (before your attack), you may leave your opponent's Active Pokémon Confused."),
        ),
        Attack(
            title='Watering',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
