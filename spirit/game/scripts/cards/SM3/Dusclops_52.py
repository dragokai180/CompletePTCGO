from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab2df1d9-e066-5c66-b776-f10ded64db54',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name',
    display_name='Dusclops',
    searchable_by=['Dusclops', 'Stage 1', 'Dusclops'],
    subtypes=['Stage 1'],
    collector_number=52,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name',
    family_id=355,
    abilities=[
        Attack(
            title='Night Roam',
            game_text="Put 1 damage counter on each Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ambush',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
