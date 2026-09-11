from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c92aeed8-b72c-5f7c-b8e4-e9b21492e29b',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name',
    display_name='Wishiwashi',
    searchable_by=['Wishiwashi', 'Basic', 'Wishiwashi'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=746,
    abilities=[
        Ability(
            title='Cowardice',
            game_text="Once during your turn (before your attack), you may discard all cards attached to this Pokémon and return it to your hand. You can't use this Ability during your first turn or on the turn this Pokémon was put into play.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
