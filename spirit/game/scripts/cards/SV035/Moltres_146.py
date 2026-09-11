from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58a8ce0a-02a7-549a-abfd-67e4f7c85158',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name',
    display_name='Moltres',
    searchable_by=['Moltres', 'Basic', 'Moltres'],
    subtypes=['Basic'],
    collector_number=146,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=146,
    abilities=[
        Ability(
            title='Flare Float',
            game_text='If this Pokémon has any Fire Energy attached, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Fire Energy attached, it has no Retreat Cost.'),
        ),
        Attack(
            title='Blazing Flight',
            game_text="Discard 2 Fire Energy from this Pokémon. This attack does 120 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 3},
            effect=standard_attack,
        ),
    ],
)
