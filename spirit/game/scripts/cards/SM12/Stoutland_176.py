from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10bc25df-b4f2-5de4-bf97-801008089b5d',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name',
    display_name='Stoutland',
    searchable_by=['Stoutland', 'Stage 2', 'Stoutland'],
    subtypes=['Stage 2'],
    collector_number=176,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name',
    family_id=506,
    abilities=[
        Ability(
            title='Arf Arf Bark',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may discard an Energy from your opponent's Active Pokémon. If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, you may discard an Energy from your opponent's Active Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Overrun',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
