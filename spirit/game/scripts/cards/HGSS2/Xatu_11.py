from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5704d2c3-79e8-5f74-bb8f-f76c18851cc2',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name',
    display_name='Xatu',
    searchable_by=['Xatu', 'Stage 1', 'Xatu'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name',
    family_id=177,
    abilities=[
        Attack(
            title='Psywave',
            game_text='Does 20 damage times the amount of Energy attached to the Defending Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Confuse Ray',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
