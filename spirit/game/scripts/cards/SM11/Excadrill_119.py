from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b2cb8b39-19a1-5a23-ad5f-3fb54fcbdc39',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name',
    display_name='Excadrill',
    searchable_by=['Excadrill', 'Stage 1', 'Excadrill'],
    subtypes=['Stage 1'],
    collector_number=119,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    family_id=529,
    abilities=[
        Attack(
            title='Rototiller',
            game_text='Shuffle 4 cards from your discard pile into your deck.',
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
