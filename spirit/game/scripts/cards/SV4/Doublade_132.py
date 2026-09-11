from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a6d096f3-169a-5963-8e42-8250ccb59ea3',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name',
    display_name='Doublade',
    searchable_by=['Doublade', 'Stage 1', 'Doublade'],
    subtypes=['Stage 1'],
    collector_number=132,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    family_id=679,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Slashing Strike',
            game_text="During your next turn, this Pokémon can't use Slashing Strike.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
