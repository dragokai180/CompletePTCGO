from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37345a7d-908f-5f25-8400-e653e0edecb5',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name',
    display_name='Gardevoir',
    searchable_by=['Gardevoir', 'Stage 2', 'Gardevoir'],
    subtypes=['Stage 2'],
    collector_number=141,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    family_id=280,
    abilities=[
        Attack(
            title='Brilliant Search',
            game_text='Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sensitive Ray',
            game_text='If you played a Supporter card from your hand during this turn, this attack does 90 more damage.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
