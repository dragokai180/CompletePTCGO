from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dcd25acc-73d0-5144-ac99-87f0f606f51d',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MVenusaurEX.Name',
    display_name='M Venusaur-EX',
    searchable_by=['M Venusaur-EX', 'MEGA', 'EX', 'MVenusaurEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=2,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name',
    family_id=3,
    abilities=[
        Attack(
            title='Bloom Buster',
            game_text="Flip a coin. If heads, this attack does 30 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
