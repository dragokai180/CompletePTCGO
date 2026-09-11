from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c86e11f5-7abb-5541-93c1-542d44f39371',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name',
    display_name='Rhyperior',
    searchable_by=['Rhyperior', 'Stage 2', 'Rhyperior'],
    subtypes=['Stage 2'],
    collector_number=67,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name',
    family_id=111,
    abilities=[
        Ability(
            title='Toppling Wind',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may discard the top 3 cards of your opponent's deck.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Rock Wrecker',
            game_text="This attack's damage isn't affected by Weakness or Resistance. This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
