from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d35e6b5e-bd05-52ad-9962-bdc4496abd67',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Musharna.Name',
    display_name='Musharna',
    searchable_by=['Musharna', 'Stage 1', 'Musharna'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name',
    family_id=517,
    abilities=[
        Attack(
            title='Dream of Memories',
            game_text='Shuffle 3 cards from your discard pile into your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dream Dance',
            game_text='Both Active Pokémon are now Asleep.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
