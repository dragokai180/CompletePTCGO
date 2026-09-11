from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bedb4eb7-a937-546c-a114-dd984e90b08a',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name',
    display_name='Hoopa',
    searchable_by=['Hoopa', 'Basic', 'Hoopa'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=720,
    abilities=[
        Attack(
            title='Hyperspace Ring',
            game_text='Search your deck for up to 2 Item cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psy Bolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
