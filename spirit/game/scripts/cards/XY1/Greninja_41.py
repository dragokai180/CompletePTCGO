from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e215f0a9-9f63-55b1-b6bd-246039c95d10',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name',
    display_name='Greninja',
    searchable_by=['Greninja', 'Stage 2', 'Greninja'],
    subtypes=['Stage 2'],
    collector_number=41,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name',
    family_id=656,
    abilities=[
        Ability(
            title='Water Shuriken',
            game_text="Once during your turn (before your attack), you may discard a Water Energy card from your hand. If you do, put 3 damage counters on 1 of your opponent's Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Mist Slash',
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
