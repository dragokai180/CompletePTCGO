from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5c3f338e-78df-5f09-87bb-8d8e1c99326a',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name',
    display_name='Slowking',
    searchable_by=['Slowking', 'Stage 1', 'Slowking'],
    subtypes=['Stage 1'],
    collector_number=48,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=199,
    abilities=[
        Attack(
            title='Drift Ashore',
            game_text='Search your deck for a card and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Unarmed',
            game_text="If you have no cards in your hand, ignore all Energy in this attack's cost.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
