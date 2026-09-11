from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='04ee1c3c-f304-53ab-891e-c55b8646dfcf',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.KrookodileEX.Name',
    display_name='Krookodile-EX',
    searchable_by=['Krookodile-EX', 'Basic', 'EX', 'KrookodileEX'],
    subtypes=['Basic', 'EX'],
    collector_number=25,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=553,
    abilities=[
        Attack(
            title='Second Bite',
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Megaton Fang',
            game_text="Discard a card from your hand. If you can't discard a card, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
