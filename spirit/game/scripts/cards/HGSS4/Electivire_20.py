from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7154a85-52ee-515a-a394-0e3116815519',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name',
    display_name='Electivire',
    searchable_by=['Electivire', 'Stage 1', 'Electivire'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    family_id=125,
    abilities=[
        Attack(
            title='Plasma',
            game_text='Search your discard pile for a Lightning Energy card and attach it to Electivire.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Thunder Shot',
            game_text="This attack does 50 damage to each of your opponent's Pokémon that has any Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            effect=standard_attack,
        ),
    ],
)
