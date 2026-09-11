from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='47441ec4-50d4-5d0d-b19d-5726a5433361',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    display_name='Poliwhirl',
    searchable_by=['Poliwhirl', 'Stage 1', 'Poliwhirl'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Knuckle Punch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
