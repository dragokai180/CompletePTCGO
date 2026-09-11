from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4801e6b-f32d-5cfa-9670-82412ba13628',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name',
    display_name='Palossand',
    searchable_by=['Palossand', 'Stage 1', 'Palossand'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name',
    family_id=769,
    abilities=[
        Ability(
            title='Wall of Sand',
            game_text='This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Absorb Vitality',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
