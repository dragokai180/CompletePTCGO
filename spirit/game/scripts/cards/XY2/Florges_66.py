from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d7d23ab-f175-548a-97f7-5a8ef710ccbc',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name',
    display_name='Florges',
    searchable_by=['Florges', 'Stage 2', 'Florges'],
    subtypes=['Stage 2'],
    collector_number=66,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name',
    family_id=669,
    abilities=[
        Attack(
            title='Brilliant Search',
            game_text='Search your deck for up to 3 cards and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Petal Blizzard',
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
