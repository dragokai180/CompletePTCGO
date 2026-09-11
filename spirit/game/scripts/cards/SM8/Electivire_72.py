from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0036d3db-c029-5e2a-bf79-de321fe1c9a9',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name',
    display_name='Electivire',
    searchable_by=['Electivire', 'Stage 1', 'Electivire'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    family_id=125,
    abilities=[
        Attack(
            title='Electrocharge',
            game_text='Search your deck for up to 2 Lightning Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='High-Voltage Knuckle',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
