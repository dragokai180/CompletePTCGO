from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='68ab8723-4359-5461-984f-0620fa67b7c2',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name',
    display_name='Moltres',
    searchable_by=['Moltres', 'Basic', 'Moltres'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=146,
    abilities=[
        Attack(
            title='Top Burner',
            game_text="Discard all Fire Energy from this Pokémon. Then, discard a card from the top of your opponent's deck for each Energy you discarded in this way.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Spin',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
