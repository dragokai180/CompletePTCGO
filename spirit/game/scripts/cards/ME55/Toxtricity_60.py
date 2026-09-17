from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b12190b4-2706-5a45-b6a5-d4d0415f2575',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name',
    display_name='Toxtricity',
    searchable_by=['Toxtricity', 'Stage 1', 'Toxtricity'],
    subtypes=['Stage 1'],
    collector_number=60,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name',
    family_id=848,
    abilities=[
        Attack(
            title='Light Punch',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title='Thunderous Bolt',
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
