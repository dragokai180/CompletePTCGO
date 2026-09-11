from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='094b7234-d265-5106-9594-988bfaffbd3c',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name',
    display_name='Hitmontop',
    searchable_by=['Hitmontop', 'Basic', 'Hitmontop'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=237,
    abilities=[
        Attack(
            title='Finishing Combo',
            game_text="You can use this attack only if your Hitmonlee used Special Combo during your last turn. This attack does 60 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
