from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec79ad8b-0063-5715-b7f0-3294e3ac77f8',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name',
    display_name='Noivern',
    searchable_by=['Noivern', 'Stage 1', 'Noivern'],
    subtypes=['Stage 1'],
    collector_number=159,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name',
    family_id=714,
    abilities=[
        Attack(
            title='Boomburst',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top card of your deck.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
