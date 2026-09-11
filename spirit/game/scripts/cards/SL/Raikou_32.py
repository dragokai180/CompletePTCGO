from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='75766f80-cf52-5dc2-9845-52a3f166b5b7',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name',
    display_name='Raikou',
    searchable_by=['Raikou', 'Basic', 'Raikou'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=243,
    abilities=[
        Attack(
            title='Booming Thunder',
            game_text='Attach a Lightning Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Electric Ball',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
