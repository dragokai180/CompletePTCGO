from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea6f24d4-b6cd-5738-a27e-4c0752a4b9bf',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name',
    display_name='Togetic',
    searchable_by=['Togetic', 'Stage 1', 'Togetic'],
    subtypes=['Stage 1'],
    collector_number=84,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name',
    family_id=175,
    abilities=[
        Attack(
            title='Shared Peace',
            game_text='Each player draws 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Dive',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
