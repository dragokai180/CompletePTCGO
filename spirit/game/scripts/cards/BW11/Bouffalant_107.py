from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="0447bb60-69a9-5219-bf9b-ca83ec36caf0",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant","Basic","Bouffalant"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Revenge",
            game_text="If any of your Pokémon were Knocked Out by damage from an opponent's attack during his or her last turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Head Charge",
            game_text="Flip a coin. If tails, this Pokémon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=bw_legacy_attack,
        ),
    ],
)
