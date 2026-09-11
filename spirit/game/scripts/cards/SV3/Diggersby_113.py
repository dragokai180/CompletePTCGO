from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a8db0b30-4bbf-5a4b-85d2-1d9d40b7829f',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diggersby.Name',
    display_name='Diggersby',
    searchable_by=['Diggersby', 'Stage 1', 'Diggersby'],
    subtypes=['Stage 1'],
    collector_number=113,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name',
    family_id=659,
    abilities=[
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Knocking Hammer',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
