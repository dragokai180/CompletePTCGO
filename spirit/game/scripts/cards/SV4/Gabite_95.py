from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9efa5877-1a6a-5bfb-8b81-2a398e1447f0',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name',
    display_name='Gabite',
    searchable_by=['Gabite', 'Stage 1', 'Gabite'],
    subtypes=['Stage 1'],
    collector_number=95,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name',
    family_id=443,
    abilities=[
        Attack(
            title='Power Blast',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
