from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='77d987f2-91fa-5503-91fa-9a775a8522ff',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name',
    display_name='Deoxys',
    searchable_by=['Deoxys', 'Basic', 'Deoxys'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title='Psypunch',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title='Genome Spiral',
            game_text='Move all Energy from this Pokémon to your Benched Pokémon in any way you like.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
