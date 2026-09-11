from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8daa3cdc-f5a8-5258-859d-7a668a18a083',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name',
    display_name='Thundurus',
    searchable_by=['Thundurus', 'Basic', 'Thundurus'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=642,
    abilities=[
        Attack(
            title='Raging Thunder Punch',
            game_text="If your opponent's Active Pokémon has a Pokémon Tool card attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Lightning Slam',
            game_text="This Pokémon can't use Lightning Slam during your next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
