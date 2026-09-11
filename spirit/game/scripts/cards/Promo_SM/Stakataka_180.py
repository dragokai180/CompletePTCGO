from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5a81c427-f77e-5480-a1f9-98a04c933ec8',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stakataka.Name',
    display_name='Stakataka',
    searchable_by=['Stakataka', 'Basic', 'Ultra Beast', 'Stakataka'],
    subtypes=['Basic', 'Ultra Beast'],
    collector_number=180,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=805,
    abilities=[
        Ability(
            title='Wall of Stone',
            game_text="If your opponent has 3 or fewer Prize cards remaining, this Pokémon's maximum HP is 200.",
            passive=standard_passive("If your opponent has 3 or fewer Prize cards remaining, this Pokémon's maximum HP is 200."),
        ),
        Attack(
            title='Top Down',
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
