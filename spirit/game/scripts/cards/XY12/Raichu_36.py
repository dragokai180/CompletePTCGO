from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='475bad35-5a3a-5d1c-a0ad-df30df6e99d9',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name',
    display_name='Raichu',
    searchable_by=['Raichu', 'Stage 1', 'Raichu'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    family_id=25,
    abilities=[
        Attack(
            title='Energize',
            game_text='Attach a Lightning Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spark Bolt',
            game_text='You may discard all Energy attached to this Pokémon. If you do, this attack does 70 more damage.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
