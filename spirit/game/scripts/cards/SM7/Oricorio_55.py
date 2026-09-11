from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cffe5289-e80d-56dc-9819-2ca577224e0e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name',
    display_name='Oricorio',
    searchable_by=['Oricorio', 'Basic', 'Oricorio'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Attack(
            title='Zappy Pom-Poms',
            game_text="This attack does 30 damage to each Pokémon-GX and Pokémon-EX (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electric Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
