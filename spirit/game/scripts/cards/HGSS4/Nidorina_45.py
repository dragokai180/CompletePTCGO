from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6bb02721-48d9-549b-96a6-df655ba48b38',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    display_name='Nidorina',
    searchable_by=['Nidorina', 'Stage 1', 'Nidorina'],
    subtypes=['Stage 1'],
    collector_number=45,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    family_id=29,
    abilities=[
        Attack(
            title='Quick Blow',
            game_text='Flip a coin. If heads, this attack does 20 damage plus 10 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Tail Slap',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
