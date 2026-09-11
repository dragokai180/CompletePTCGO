from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b890ebb3-2746-5bd5-b4f7-d31a75b157b9',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name',
    display_name='Fearow',
    searchable_by=['Fearow', 'Stage 1', 'Fearow'],
    subtypes=['Stage 1'],
    collector_number=98,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    family_id=21,
    abilities=[
        Attack(
            title='Devastating Wind',
            game_text='Your opponent shuffles their hand into their deck and draws 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Strike',
            game_text="This Pokémon can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
