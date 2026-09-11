from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5faf6df-e157-5f02-96f0-da1244811cde',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    display_name='Fletchinder',
    searchable_by=['Fletchinder', 'Stage 1', 'Fletchinder'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Heat Dive',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
