from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='93546a54-6af5-5a6e-a1c1-d0ea6a43949a',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floatzel.Name',
    display_name='Floatzel',
    searchable_by=['Floatzel', 'Stage 1', 'Floatzel'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    family_id=418,
    abilities=[
        Attack(
            title='Hydro Pump',
            game_text='This attack does 20 more damage for each Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
