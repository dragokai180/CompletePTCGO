from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bbe0558d-44c1-5a3c-9b72-76a80433610d',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name',
    display_name='Kadabra',
    searchable_by=['Kadabra', 'Stage 1', 'Kadabra'],
    subtypes=['Stage 1'],
    collector_number=64,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name',
    family_id=63,
    abilities=[
        Attack(
            title='Teleportation Attack',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
