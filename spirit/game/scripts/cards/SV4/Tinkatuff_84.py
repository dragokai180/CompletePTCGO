from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='adafb80f-665f-5ef2-843e-336b043586eb',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name',
    display_name='Tinkatuff',
    searchable_by=['Tinkatuff', 'Stage 1', 'Tinkatuff'],
    subtypes=['Stage 1'],
    collector_number=84,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name',
    family_id=957,
    abilities=[
        Attack(
            title='Alloy Aswing',
            game_text='If this Pokémon has any Metal Energy attached, this attack does 40 more damage.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
