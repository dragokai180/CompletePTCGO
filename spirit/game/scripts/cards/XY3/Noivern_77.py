from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a38c5d6-8e2b-503c-9ac9-b1701ef52eb4',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name',
    display_name='Noivern',
    searchable_by=['Noivern', 'Stage 1', 'Noivern'],
    subtypes=['Stage 1'],
    collector_number=77,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name',
    family_id=714,
    abilities=[
        Ability(
            title='Echolocation',
            game_text='If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.',
            passive=standard_passive('If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.'),
        ),
        Attack(
            title='Boomburst',
            game_text="This attack does 30 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
