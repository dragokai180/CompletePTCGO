from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92f3fcf4-c07d-500a-ad7a-75cf755cf78f',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.JirachiGX.Name',
    display_name='Jirachi-GX',
    searchable_by=['Jirachi-GX', 'Basic', 'GX', 'JirachiGX'],
    subtypes=['Basic', 'GX'],
    collector_number=79,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=385,
    abilities=[
        Ability(
            title='Psychic Zone',
            game_text="Don't apply Psychic Weakness when Pokémon (both yours and your opponent's) take damage from attacks.",
            passive=standard_passive("Don't apply Psychic Weakness when Pokémon (both yours and your opponent's) take damage from attacks."),
        ),
        Attack(
            title='Star Search',
            game_text='Search your deck for an Energy card and attach it to 1 of your Psychic Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Star Shield-GX',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            effect=standard_attack,
            locks_next_turn=False,
            gx=True,
        ),
    ],
)
