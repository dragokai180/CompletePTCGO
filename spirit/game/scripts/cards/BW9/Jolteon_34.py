from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import call_for_family, comet_punch
from spirit.game.card_effects.pokemon import blizzard_bind, regi_gate
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="8168e223-f384-5b6e-b8e4-ae62a5c3bae9",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon","Stage 1","Jolteon"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=comet_punch,
        ),
        Attack(
            title="Electri-Defuse",
            game_text="If the Defending Pokémon is a Pokémon-EX, that Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=blizzard_bind,
        ),
    ],
)
