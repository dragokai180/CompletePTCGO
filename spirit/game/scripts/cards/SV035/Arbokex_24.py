from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc6d8d36-618c-54c4-82fd-0d3fc9a4f35f',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arbokex.Name',
    display_name='Arbok ex',
    searchable_by=['Arbok ex', 'Stage 1', 'ex', 'Arbokex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=24,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name',
    family_id=23,
    abilities=[
        Attack(
            title='Bind Down',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Menacing Fangs',
            game_text='Your opponent discards 2 cards from their hand.',
            cost={PokemonTypes.DARKNESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
